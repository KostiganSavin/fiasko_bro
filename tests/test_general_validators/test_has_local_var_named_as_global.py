from fiasko_bro import validators
from fiasko_bro.code_validator import CodeValidator
from fiasko_bro.i18n import _


def test_has_local_var_named_as_global_fail(test_repo):
    expected_output = 'has_locals_named_as_globals', _('for example, %s') % 'LOCAL_VAR'
    whitelists = CodeValidator.whitelists
    output = validators.has_local_var_named_as_global(
        solution_repo=test_repo,
        whitelists=whitelists,
        max_indentation_level=CodeValidator._default_settings['max_indentation_level']
    )
    assert output == expected_output


def test_has_local_var_named_as_global_ok(test_repo):
    whitelists = {'has_local_var_named_as_global': [
        'local_var_as_global_test_file.py'
    ]}
    max_indentation_level = CodeValidator._default_settings[
        'max_indentation_level'
    ]
    output = validators.has_local_var_named_as_global(
        solution_repo=test_repo,
        whitelists=whitelists,
        max_indentation_level=max_indentation_level,
    )
    assert output is None
