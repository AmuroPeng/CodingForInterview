/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
  if (!lists.length) return null;
  let dummy = new ListNode();
  let p = dummy;
  var pq = new MinPriorityQueue({ priority: (node) => node.val});

  for (var i = 0; i < lists.length; i += 1) {
      if (lists[i]) pq.enqueue(lists[i]);
  }
  while(!pq.isEmpty()) {
      let node = pq.dequeue().element;
      p.next = node;
      if (node.next) {
          pq.enqueue(node.next);
      }
      p = p.next;
  }
  return dummy.next;
};