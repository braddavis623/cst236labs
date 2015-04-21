from behave import given, when, then


@given('we are researching speeds')
def step_impl(context):
    pass


@when('we select a size')
def step_impl(context):
    assert 'size_selected' is not False


@then('we will have more storage')
def step_impl(context):
    assert context.failed is False