# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables coding, blockchain coding, and a short interview covering parts of hash tables and blockchain.

## Interview Questions

During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following two topics:

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?
* What is the worse case scenario if you try to extend the storage size of a dynamic array?

Explain how blockchain networks remain in consensus:
* What does a node do if it gets a message from another in the network with a new block?
    When a solution is discovered, a block is mined and it is added to the chain by the node that discovered it, or the first one it was reported to - assuming the node finds the solution to be valid. If it is a valid solution, the node will hash the previous block and add it to the new block, and add the rest of the properties, including a timestamp, index, and the list of pending transactions, which are now confirmed. It then shares the new block with the nodes in its network, which check the new block to make sure that it has an index one higher than the last block, a previous hash that matches the previous block, and a valid solution. If these checks pass, then the new block is added and spreads through the network, bearing in mind that consensus is determined by the longest valid chain.
* Why can't someone cheat by changing a transaction from an earlier block to give themselves coins?
    This distribution means that the chain itself is nearly impossible to assault. We’ve learned that to change the chain itself, we need to redo the previous hash stored in all subsequent blocks. But as described above, it would take a vast amount of computing power to do so.
    Let’s say the chain is on block 1000, and we want to make a change to a transaction stored in block 98 to change a record in the ledger to give money to ourselves, instead of the intended recipient. Making this change is trivial, we simply open up our copy of the blockchain and edit the transaction.

    However, we now have a problem. The previous hash stored in block 99 now no longer matches the hash of block 98. If you change even one character or digit, the hash is completely different. So if we try to share our changed blockchain as the valid one, everyone will reject it because it has a bad hash.

    We could just chop off the the bad hash, but then our chain gets rejected because it’s not the longest. The only recourse would be to mine new blocks and make a longer chain.
    This still doesn’t help. The biggest problem is that we are not alone. Everyone else mining is adding to the end of the chain. So not only do we need the hardware to solve this problem, but we need to outrun everyone else, because every 10 minutes, they add another block to the chain and move the goalpost farther away.
    

## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced, built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables)

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain)


### Rubric

| *OBJECTIVE*                                                                                                     | *TASK*             | *1 - DOES NOT MEET EXPECTATIONS*                                                                                            | *2 - MEETS EXPECTATIONS*                                                                                                       | *3 - EXCEEDS EXPECTATIONS                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| implement and describe how high-level array functions work down to the memory level                             | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| implement and utilize basic hash table + handle collisions and resizing in a hash table                         | Hash Problem 1 & 2 | Tests do not pass on one or both problems, or solutions do not use hash tables.                                             | Tests pass on both problems.  Solution utilizes a hash table.                                                                  | Tests pass on on both problems with solutions utilizing hash tables, linear runtime complexity, no flake8 complaints.                                 |
| diagram and code a simple blockchain, utilizing a cryptographic hash                                            | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
| utilize a Proof of Work process to protect a blockchain from attack                                             | Blockchain Problem | The student is unable to mine a coin before the end of lunch.                                                               | The student was able to mine a coin before the end of lunch.                                                                   | The student presented a unique solution that was able to mine more than 100 coins before the end of lunch.                                            |
| build a protocol to allow nodes in a blockchain network to communicate to share blocks and determine consensus. | Interview Question | The student fully explains two or fewer of the bulleted items in the solution repo\. | The student fully explains at least 3 of the items in the bulleted list\.                                | The student fully explains 4 or more items from the bulleted list\.           |
