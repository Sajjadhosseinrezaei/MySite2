from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Project


@receiver(post_delete, sender=Project)
def delete_project_image(sender, instance, **kwargs):
    """
    Delete the image file from the filesystem when the Project instance is deleted.
    """
    if instance.image:
        # Check if the file exists before attempting to delete it
        try:
            instance.image.delete(save=False)
        except Exception as e:
            print(f"Error deleting file: {e}")