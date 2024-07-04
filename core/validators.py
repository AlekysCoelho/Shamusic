import magic
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateImageFileExtensionAndMineType:
    """Sets validation of allowed images types."""

    extensions = ["png", "jpeg", "jpg"]
    allowed_mime_type = ["image/png", "image/jpeg"]

    def __call__(self, value):
        """Validates allowed extensions and also checks the MIME type"""
        extension_validator = FileExtensionValidator(allowed_extensions=self.extensions)
        extension_validator(value)

        mime_type = magic.Magic(mime=True)
        detected_mime_type = mime_type.from_buffer(value.read(1024))
        value.seek(0)

        if detected_mime_type not in self.allowed_mime_type:
            raise ValidationError("The file is not a valid PNG or JPEG image.")


validate_image_extension_and_mime_type = ValidateImageFileExtensionAndMineType()
