public class SeniorClass {
  public SeniorClass(){
      toString(); //may throw NullPointerException if overridden
  }
  public String toString(){
    return "IAmSeniorClass";
  }
}
