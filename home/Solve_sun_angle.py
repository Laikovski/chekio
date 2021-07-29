
def sun_angle(time):
    if 600 <= int(time.replace(':', '')) <= 1800:
        h, m = map(int, time.split(':'))
        minute = (h - 6) * 60 + m
        return int(angle_in_minute * minute)
    return 'I don\'t see the sun!'


angle_in_minute = 180 / (12 * 60)

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))