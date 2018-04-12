public class FooTest extends TestCase {
    void testCode() {
        Object a, b;
        assertTrue(a.equals(b));                    // bad usage
        assertEquals(?a should equals b?, a, b);    // good usage
    }
}