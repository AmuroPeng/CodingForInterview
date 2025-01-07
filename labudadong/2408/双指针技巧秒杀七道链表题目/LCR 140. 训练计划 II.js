/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} cnt
 * @return {ListNode}
 */
var trainingPlan = function(head, cnt) {
  let p1 = head, p2 = head;
  for (let i = 0; i < cnt; i += 1) {
      p1 = p1.next;
  }
  while (p1) {
      p1 = p1.next;
      p2 = p2.next;
  }
  return p2;
};