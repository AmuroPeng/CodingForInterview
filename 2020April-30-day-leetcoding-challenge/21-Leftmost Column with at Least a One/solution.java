// https://medium.com/2020-april-30-day-leetcoding-challenge/30-day-leetcoding-challenge-day-21-leftmost-column-with-at-least-a-one-8c30d4cd3327

public class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {

        List<Integer> dimensions = binaryMatrix.dimensions();
        int n = dimensions.get(0);
        int m = dimensions.get(1);

        int i = 0;
        int j = m - 1;
        int leftmost = -1;

        while (i < n && j >= 0) {

            if (binaryMatrix.get(i, j) == 1) {
                leftmost = j;
                j--; // move left
            } else {
                i++; // move down
            }

        }

        return leftmost;
    }

}