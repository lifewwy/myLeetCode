#
# A website domain like "discuss.leetcode.com" consists of various subdomains.
# At the top level, we have "com", at the next level, we have "leetcode.com",
# and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com",
# we will also visit the parent domains "leetcode.com" and "com" implicitly.
#
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
# followed by a space, followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
#
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains,
# (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.


# Example 1:
# Input:
#   ["9001 discuss.leetcode.com"]
# Output:
#   ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# Explanation:
#      We only have one website domain: "discuss.leetcode.com".
#      As discussed above, the subdomain "leetcode.com" and "com" will also be visited.
#      So they will all be visited 9001 times.

# Example 2:
# Input:
#   ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output:
#   ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation:
#   We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
#   For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.

# Notes:
#   The length of cpdomains will not exceed 100.
#   The length of each domain name will not exceed 100.
#   Each address will have either 1 or 2 "." characters.
#   The input count in any count-paired domain will not exceed 10000.
#   The answer output can be returned in any order.


# 知识点
# 1）列表的遍历
# 2）字符串 -> 列表，l = str.split(分割符)
# 3）列表 -> 字符串，s = 连接符.join(l)
# 4）dict.get(key, default=None)，由键查值
#    参数  key -- 字典中要查找的键。
#         default -- 如果指定键不存在时，返回该默认值。
# 5）列表推导式
class Solution: # wangwy
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        d = {}
        for i in cpdomains:
            count, domain = i.split(" ")
            frags = domain.split('.')
            for k in range(len(frags)):
                s = '.'.join(frags[k:])
                # print(s)
                d[s] = int(count)+d.get(s,0)

        # 字典的遍历
        return [str(v) + ' ' + k for k,v in d.items()]

# ------------------------------------------------ 网络答案 ------------------------------------------------------

from collections import defaultdict
class Solution1:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = defaultdict(int)
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            curr = []
            for i in reversed(range(len(frags))):
                curr.append(frags[i])
                result[".".join(reversed(curr))] += count

        # return ["{} {}".format(count, domain) for domain, count in result.items()]
        return [str(count) + ' ' + domain for domain, count in result.items()]

# -----------------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
























