from pathlib import Path
from uuid import UUID

from moxn.client import MoxnClient
from moxn.exceptions import MoxnSchemaValidationError


class SchemaGenerator:
    """
    Schema generator for writing API-generated typed models into user codebases.

    Example:
        ```python
        from moxn.schema_generator import SchemaGenerator

        generator = SchemaGenerator()
        await generator.generate_schema(
            request_id="your-request-id",
            version_id="your-version-id",
            output_dir="./my_types"
        )
        ```
    """

    async def generate_schema(
        self,
        request_id: str | UUID,
        version_id: str | UUID | None = None,
        output_dir: str | Path = Path("./moxn/types"),
    ) -> list[Path]:
        """
        Generate schema models for a specific request version.

        Args:
            request_id: The request ID
            version_id: The request version ID
            output_dir: Directory where schema files will be written

        Returns:
            List of paths to generated schema files

        Raises:
            MoxnSchemaValidationError: If schema validation fails
        """
        # Convert output_dir to Path
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Fetch generated code from API
        async with MoxnClient() as client:
            url = f"schemas/{request_id}/codegen"
            if version_id:
                url += f"?version_id={version_id}"
            response = await client.get(url)

            if response.status_code == 404:
                raise KeyError(
                    f"Request {request_id} or version {version_id} not found"
                )

            response.raise_for_status()

            try:
                generated_files: dict[str, str] = response.json()
            except Exception as e:
                raise MoxnSchemaValidationError(
                    request_id=str(request_id),
                    version_id=str(version_id),
                    schema=response.text,
                    detail=str(e),
                )

        written_files: list[Path] = []

        # Write each generated file to the output directory
        for filename, content in generated_files.items():
            file_path = output_dir / filename
            file_path.write_text(content)
            written_files.append(file_path)

        # Create __init__.py to make the directory a package
        init_file = output_dir / "__init__.py"
        init_file.touch()
        written_files.append(init_file)

        return written_files
