"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
        
    if numbers[0] >= numbers[1]:
        primeiro = 0
        segundo = 1
    else:
        primeiro = 1
        segundo = 0
    for i in range(2, len(numbers)):
        if numbers[i] > numbers[primeiro]:
            segundo = primeiro
            primeiro = i
        elif numbers[i] > numbers[segundo]:
            segundo = i
    

    return numbers[segundo], numbers[primeiro]
