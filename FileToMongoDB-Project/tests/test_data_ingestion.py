import pytest
import config

dbname = config.MONGODB_DATABASE
assert(isinstance(config.MONGODB_PORT, int))
