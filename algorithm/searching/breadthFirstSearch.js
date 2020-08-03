
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
 
