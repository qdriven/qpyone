from dynaconf import Dynaconf


settings = Dynaconf(
    envar_prefix="fluent",
    settings_file=["configs/settings.toml", "configs/.secrets.toml"],
    environment=True,
    load_dotenv=True,
    dotenv_path="/.env",  # custom path for .env file to be loaded
    includes=["../config/custom_settings.toml"],
)

settings.validators.validate()
