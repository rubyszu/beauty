public class TestAdd{
    Logger log = Logger.getLogger(Foo.class.getName());                 // not recommended

    static final Logger log = Logger.getLogger(Foo.class.getName());    // preferred approach
}