import piltdown.literals as lit
import piltdown.util as util
import piltdown.hdot_chart as hdot

# Example horizontal dot chart:

print(
    "How many times I ate chocolate this week:\n\n"
    + hdot.hdot_chart(
        [3, 2, 4, 0, 2, 1, 4], ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    )
)
