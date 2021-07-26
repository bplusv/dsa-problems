from datetime import datetime, timezone
import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp or datetime.now(tz=timezone.utc).isoformat()
        self.data = data or ''
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.timestamp.encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        sha.update(self.previous_hash.encode('utf-8'))
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, timestamp, data):
        previous_hash = self.tail.hash if self.tail else '0'
        new_block = Block(timestamp, data, previous_hash)
        if self.tail:
            self.tail.next = new_block
        self.tail = new_block
        if not self.head:
            self.head = new_block

    def __repr__(self):
        output = ''
        curr = self.head
        while curr:
            output += '-' * 70 + '\n'
            output += f'hash: {curr.hash}\n'
            output += f'prev: {curr.previous_hash}\n'
            output += '-' * 70 + '\n'
            output += f'{curr.timestamp}: {curr.data}\n'
            output += '-' * 70 + '\n'
            curr = curr.next
        return output


def test_case_1():
    print('--- testcase 1 ---')
    my_blockchain = BlockChain()
    my_blockchain.append('2020-12-01T20:00:12.274510+00:00', 'Single block edge case')
    print(my_blockchain)


def test_case_2():
    print('--- testcase 2 ---')
    my_blockchain = BlockChain()
    # empty and null values test case
    my_blockchain.append(None, '')
    my_blockchain.append('', None)
    print(my_blockchain)


def test_case_3():
    print('--- testcase 3 ---')
    my_blockchain = BlockChain()
    my_blockchain.append('2020-12-01T20:00:12.274510+00:00', 'Bob pays Alice $50')
    my_blockchain.append('2020-12-02T15:59:19.131710+00:00', 'Alice pays Bob $25')
    my_blockchain.append('2020-12-03T01:23:49.378419+00:00', 'Joe pays Grace $100')
    my_blockchain.append('2020-12-04T07:12:50.892030+00:00', 'Grace pays Joe $10')
    my_blockchain.append('2020-12-05T03:48:01.193866+00:00', 'Grace pays Joe $90')
    my_blockchain.append('2020-12-06T17:21:33.578497+00:00', 'Alice pays Bob $25')
    print(my_blockchain)


test_case_1()

test_case_2()

test_case_3()
