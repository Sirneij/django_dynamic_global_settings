"""
Name: Idogun, John Owolabi

E-mail address: sirneij@gmail.com
"""


def get_maximum_amount_of_money(house_wealth: list[int]) -> int:
    if len(house_wealth) <= 0:
        return 0
    if len(house_wealth) == 1:
        return house_wealth[0]
    if len(house_wealth) == 2:
        return max(house_wealth[0], house_wealth[1])

    dp: list[int] = [house_wealth[0], max(house_wealth[0], house_wealth[1])]

    for i in range(2, len(house_wealth)):
        dp.append(max(house_wealth[i] + dp[i - 2], dp[i - 1]))

    return dp[len(house_wealth) - 1]


print(get_maximum_amount_of_money([2, 5, 1, 3, 6, 2, 4]))
print(get_maximum_amount_of_money([2, 10, 14, 8, 1]))
