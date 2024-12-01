file = open("input.txt", "r")

lists = file.readlines()
lists = [l.split("   ") for l in lists]
left_list = [int(l[0]) for l in lists]
right_list = [int(l[1]) for l in lists]

left_list.sort()
right_list.sort()

distance_apart = [abs(x - y) for x, y in zip(left_list, right_list)]

distance_sum = sum(distance_apart)

print("the distance between lists is: " + str(distance_sum))


# part 2

def fill_hist(lst, hist):
    i = 0
    while i < len(lst):
        x = lst[i]
        while i < len(lst) and lst[i] == x:
            hist[x] += 1
            i += 1


hist_size = max(left_list[-1], right_list[-1]) + 1

left_hist = [0 for i in range(hist_size)]
right_hist = [0 for i in range(hist_size)]

fill_hist(left_list, left_hist)
fill_hist(right_list, right_hist)

sim_scores = [i*left_hist[i]*right_hist[i] for i in range(hist_size)]
sim_sum = sum(sim_scores)

print("the final similarity score is: " + str(sim_sum))
