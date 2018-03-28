import java.util.Scanner;

package heaps;

import java.util.ArrayList;
import java.util.List;

/**
 * Heap tree where a node's key is higher than or equal to its parent's and lower than or equal
 * to its children's.
 * @author Nicolas Renard
 *
 */
public class MaxHeap implements Heap {
    
    private final List<HeapElement> maxHeap;
    
    public MaxHeap(List<HeapElement> listElements) throws Exception {
        maxHeap = new ArrayList<HeapElement>();
        for (HeapElement heapElement : listElements) {
            if (heapElement != null) insertElement(heapElement);
            else System.out.println("Null element. Not added to heap");
        }
        if (maxHeap.size() == 0) System.out.println("No element has been added, empty heap.");
        }
    
    // Get the element at a given index. The key for the list is equal to index value - 1
    public HeapElement getElement(int elementIndex) {
        if ((elementIndex <= 0) && (elementIndex > maxHeap.size())) throw new IndexOutOfBoundsException("Index out of heap range");
        return maxHeap.get(elementIndex - 1);
    }