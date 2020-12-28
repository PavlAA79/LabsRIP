from radish import given, when, then
from IcecreamBuilder import Type1IcecreamBuilder

@given("I am creating Type1 Builder")
def create_type1builder(step):
    step.context.builder = Type1IcecreamBuilder()

@when("I make him do cream only icecream")
def builder_produce_only_cream(step):
    step.context.builder.produce_cream()

@then("Then I expect that cream will be {cream_name: w}")
def expect_cream_name(step, cream_name):
    assert step.context.icecream.cream == [cream_name]