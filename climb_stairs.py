def climbstairs(n):
    previous_calculations = {}  # init memoization map

    def track_count(n, previous_calculations):

        if (n == 0):
            return 1
        elif n < 0:
            return 0

        if(previous_calculations[n]):
            return previous_calculations[n]
        else:
            previous_calculations[n] = track_count(
                n+1, previous_calculations) + track_count(n+2, previous_calculations)
            return previous_calculations[n]  # return memoized value

        return track_count(n, previous_calculations)


if __name__ == "__main__":
    a = climbstairs(4)
    print(a)
    climbstairs(5)
