def remove_parentheses(s):
    char_temp_list_left = []
    s_list = list(s)

    while '(' in s_list:
        for idxl, char in enumerate(s_list):
            if char == '(':
                char_temp_list_left.append(idxl)
            if char == ')':
                for idxr, pr in enumerate(s_list):
                    if pr == ')':
                        s_temp = s[char_temp_list_left[-1]:idxr+1]
                        s = s.replace(s_temp, '')
                        s_list = list(s)
                        char_temp_list_left = []
                        break
                break

    return s


# print(remove_parentheses("hello example (words(more words) here) something"))
# remove_parentheses("hello example (words(mo(test)re (cos) words) here) (test2) something")
# remove_parentheses("(first group) (second group) (third group)")
# remove_parentheses("example(unwanted thing)example")
# remove_parentheses("a (bc d)e")
# remove_parentheses("example (unwanted thing) example")
print(remove_parentheses('(cneEBuzmrnWmNEmWFK)o((RKKaIAhBSpkHcc ))(grRAHiSjykq(OtqedZ jUkYuBGwyykTqMB()NS)ZUHmtJ)(YGOnR)DhR(tFbYZhtkKrSSzV(wVORwbXmfKfkNDVg)dNoIY)jycFQ()ItM ARQXv( f(WzIVoY DKSBpdlKbYNzwc)xHs(XeRqF EhnDJLPyt Ze)BtFnFNe(u)wCoed)OQgFzr mA JQP(lpfo(PMZN)kyjsYTVtngogfVEdbY)WE(Il) BC'))
