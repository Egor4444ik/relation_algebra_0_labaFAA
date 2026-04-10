def main(input_data):
	stdin = input_data.get('stdin', '')

	numbers = list(map(int, stdin.split()))
	result = sum(numbers)
	return {'stdout': str(result)}
