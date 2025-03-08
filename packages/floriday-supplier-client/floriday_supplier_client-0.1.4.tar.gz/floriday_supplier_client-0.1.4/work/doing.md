# Doing

## Goal
Fix the hardcoded staging URL in Configuration class to ensure the API client uses the correct base URL from environment variables.

## Analysis
- The `Configuration` class in the `floriday_supplier_client` package has a hardcoded staging URL as the default host
- This causes issues when using the client in a production environment as API calls will be directed to the staging API
- The `ApiFactory` class reads the base URL from environment variables but doesn't set it in the configuration
- Current workaround requires manually setting the host after client initialization

## Design
Modify the `_configure_client` method in the `ApiFactory` class to set the host in the configuration to the base URL from environment variables.

## Steps
1. Update doing.md with current work (this file)
2. Modify api_factory.py to set configuration.host = self.base_url
3. Add test to verify host configuration
4. Test the changes with both staging and production URLs
5. Create commit with descriptive message

## Progress
- [x] Update doing.md
- [x] Modify api_factory.py to set configuration.host = self.base_url
- [x] Add test to verify host configuration
- [x] Test the changes with both staging and production URLs
- [x] Create commit with descriptive message
