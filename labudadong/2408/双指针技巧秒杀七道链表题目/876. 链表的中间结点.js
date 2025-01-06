/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
  let p1 = head;
  let p2 = head;
  while (p1?.next) {
      p1 = p1.next;
      p2 = p2.next;
      if (p1) p1 = p1.next;
  }
  return p2;
};

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
  let l = head;
  let r = head;
  while (r && r.next) {
      l = l.next;
      r = r.next.next;
  }
  return l;
};