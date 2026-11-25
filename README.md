# test-shipyard-fixtures

Stock Laravel apps as students commit them (with composer.lock), one per
branch, deployed by Shipyard's `e2e/version_matrix.py`:

- `laravel-10`: Laravel 10, `"php": "^8.2"` (8.1 is below Railpack's minimum)
- `laravel-11`: Laravel 11, unchanged

Locks resolved for PHP 8.2 on 2026-11-25. Not for real use: both versions
are past security support.
