/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
  let dummyL = new ListNode();
  let dummyR = new ListNode();
  let pL = dummyL;
  let pR = dummyR;
  while (head) {
      if (head.val < x) {
          pL.next = head;
          pL = pL.next;
      } else {
          pR.next = head;
          pR = pR.next;
      }
      head = head.next;
  }
  pR.next = null;
  pL.next = dummyR.next;
  return dummyL.next;
};