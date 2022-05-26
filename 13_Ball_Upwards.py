def max_ball(v0):
    v_m_s = (v0 * 1000) / 3600
    t = 0
    h_act = 0
    h_prev = 0
    g = 9.81
    while True:
        h_act = (v_m_s * t) - ((g * pow(t, 2)) / 2)
        if h_act < h_prev:
            print(f'[m/s] = {v_m_s}')
            return h_prev, round(t * 10 - 1)
        h_prev = h_act
        t += 0.1
        print(f'h_act = {h_act} [m], t = {t} [s]')


print(max_ball(37))
print('*' * 100)
print(max_ball(45))
print('*' * 100)
print(max_ball(99))
print('*' * 100)
print(max_ball(85))
