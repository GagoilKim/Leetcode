import java.util.ArrayList;

import java.util.List;
class AddTwoNumbers{
public static void main(final String[] args) {
    public final ListNode addTwoNumbers(final ListNode l1, final ListNode l2) {
        final ArrayList<Integer> num1 = new ArrayList<>();
        final ArrayList<Integer> num2 = new ArrayList<>();
        while(l1.next != null){
            num1.add(0, l1.val);
            l1 = l1.next;
        }
        while(l2.next != null){
            num2.add(0, l2.val);
            l2 = l2.next;
        }
        int n1 = Integer.parseInt(num1.toString());
        int n2 = Integer.parseInt(num2.toString());
        String sum = Integer.toString(n1 + n2);
        char[] array = sum.toCharArray();
        ListNode start = new ListNode((int)array[array.length -1]);
        ListNode node = start;
        for(int i = array.length -2 ; i  >= 0; i --){
            ListNode tmp = new ListNode((int)array[i]);
            node.next = tmp;
            node = node.next;
        }
    }
}
public class ListNode {
         int val;
         ListNode next;
         ListNode() {}
         ListNode(final int val) { this.val = val; }
         ListNode(final int val, final ListNode next) { this.val = val; this.next = next; }
     }
}