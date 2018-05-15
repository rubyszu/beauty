public class parent {
    int value ; 
}

public class child extends parent {
    int childValue;
    public child(){}
    public child (int value){
          this.childValue = value ; // this line cause ConstructorCallsOverridableMethod warning during object construction
    }
}