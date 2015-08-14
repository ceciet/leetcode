__author__ = 'baidu'
class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (C-A)*(D-B) + (G-E)*(H-F)
        A1 = max(A, E)
        B1 = max(B, F)
        C1 = min(C, G)
        D1 = min(D, H)
        if D1 <= B1 or C1 <= A1:
            return area
        return area - (D1 - B1) * (C1 - A1)
