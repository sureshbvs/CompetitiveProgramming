import unittest
def find_repeat(the_list):
    a=1
    b=len(the_list)-1
    while a<b:
        midpoint=a+((b-a)/2)
        lowerrange_a, lowerrange_b=a,midpoint
        upperrange_a,upperrange_b= midpoint+1,b
        c=0
        for i in the_list:
            if i>=lowerrange_a and i<=lowerrange_b:
                c+= 1
        d=(lowerrange_b-lowerrange_a+1)
        if c>d:
            
            a,b=lowerrange_a,lowerrange_b
        else:
            
            a,b=upperrange_a,upperrange_b

    
    return a

 // tests

    @Test
    public void justTheRepeatedNumberTest() {
        final int[] numbers = {1, 1};
        final int expected = 1;
        final int actual = findRepeat(numbers);
        assertEquals(expected, actual);
    }

    @Test
    public void shortArrayTest() {
        final int[] numbers = {1, 2, 3, 2};
        final int expected = 2;
        final int actual = findRepeat(numbers);
        assertEquals(expected, actual);
    }

    @Test
    public void mediumArrayTest() {
        final int[] numbers = {1, 2, 5, 5, 5, 5};
        final int expected = 5;
        final int actual = findRepeat(numbers);
        assertEquals(expected, actual);
    }

    @Test
    public void longArrayTest() {
        final int[] numbers = {4, 1, 4, 8, 3, 2, 7, 6, 5};
        final int expected = 4;
        final int actual = findRepeat(numbers);
        assertEquals(expected, actual);
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
