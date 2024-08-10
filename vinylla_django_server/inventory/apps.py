from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"

    def ready(self) -> None:
        from django.core.management import call_command

        try:
            call_command("create_data")
        except Exception as e:
            print(e)
