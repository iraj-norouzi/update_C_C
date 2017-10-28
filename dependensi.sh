#!/bin/bash
psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.33_upgrade.sql
psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.34_upgrade.sql
psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.35_upgrade.sql
psql -U ibs IBSng < /usr/local/IBSng/db/from_B1.36_upgrade.sql
psql -U ibs IBSng < /usr/local/IBSng/db/defs.sql
psql -U ibs IBSng < /usr/local/IBSng/db/table.sql
psql -U ibs IBSng < /usr/local/IBSng/db/function.sql
python /usr/local/IBSng/scripts/python_dependency_setup.py install
