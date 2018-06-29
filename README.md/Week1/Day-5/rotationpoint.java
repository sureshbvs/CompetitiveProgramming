import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static int findRotationPoint(String[] words) 
    {

        // find the rotation point in the array
        int l=words.length;
       int start=0;
       int end=l-1;
       int mid=start+(end-start)/2;
       return b_search(words,start,end,mid);
    }
public static int b_search(String [] words, int start, int end, int mid){
        if (start>=end)
            return mid;
        if (words[mid].compareTo(words[end]) > 0){
            start=mid+1;
            mid=start+(end-start)/2;
            return b_search(words, start, end, mid);
        }
        if (words[mid].compareTo(words[start]) < 0){
            end=mid;
            mid=start+(end-start)/2;
            return b_search(words, start, end, mid);
        }
        throw new IllegalArgumentException();
            
    }
    // tests

    @Test
    public void smallArrayTest() {
        final int actual = findRotationPoint(new String[] {"cape", "cake"});
        final int expected = 1;
        assertEquals(expected, actual);
    }

    @Test
    public void mediumArrayTest() {
        final int actual = findRotationPoint(new String[] {"grape", "orange", "plum",
            "radish", "apple"});
        final int expected = 4;
        assertEquals(expected, actual);
    }

    @Test
    public void largeArrayTest() {
        final int actual = findRotationPoint(
            new String[] {"ptolemaic", "retrograde", "supplant", "undulate", "xenoepist",
            "asymptote", "babka", "banoffee", "engender", "karpatka", "othellolagkage"});
        final int expected = 5;
        assertEquals(expected, actual);
    }

    @Test
    public void possiblyMissingEdgeCaseTest() {
        // are we missing any edge cases?
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}

