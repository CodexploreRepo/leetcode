class Node {
  constructor(value) {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(value) {
    const newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
    } else {
      let currentNode = this.root;
      while (true) {
        if (value < currentNode.value) {
          //Left
          if (!currentNode.left) {
            currentNode.left = newNode;
            return this;
          }
          currentNode = currentNode.left;
        } else {
          //Right
          if (!currentNode.right) {
            currentNode.right = newNode;
            return this;
          }
          currentNode = currentNode.right;
        }
      }
    }
  }
  lookup(value) {
    if (!this.root) {
      return false;
    }
    let currentNode = this.root;
    while (currentNode) {
      if (value < currentNode.value) {
        currentNode = currentNode.left;
      } else if (value > currentNode.value) {
        currentNode = currentNode.right;
      } else if (currentNode.value === value) {
        return currentNode;
      }
    }
    return null;
  }
 
  //<-----BFS using While Loop---->
  breadthFirstSearch() {
    let currentNode = this.root;
    let list = [];
    let queue = [];

    //Keep track the current Node
    queue.push(currentNode);

    while (queue.length > 0) {
      //Shift() means return and remove the first item in the queue
      currentNode = queue.shift();
      //console.log(currentNode.value);
      list.push(currentNode.value);
      //Add the left child of current node to the queue
      if (currentNode.left) {
        queue.push(currentNode.left);
      }
      if (currentNode.right) {
        queue.push(currentNode.right);
      }
    }
    return list;
  }
  
  //<-----BFS using Recursion---->
  breadthFirstSearchR(queue, list) {
    if (!queue.length) {
      return list;
    }
    //Shift() means return and remove the first item in the queue
    const currentNode = queue.shift();
    //console.log(currentNode.value);
    list.push(currentNode.value);
    //Add the left child of current node to the queue
    if (currentNode.left) {
      queue.push(currentNode.left);
    }
    if (currentNode.right) {
      queue.push(currentNode.right);
    }

    return this.breadthFirstSearchR(queue, list);
  }
 
const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
//tree.remove(170);
JSON.stringify(traverse(tree.root));
//console.log(tree.breadthFirstSearch());
//console.log(tree.breadthFirstSearchR([tree.root], []));
console.log(tree.DFSPostOrder());

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
