import random

# สร้างตัวแปรชื่อ queue ไว้เก็บข้อมูลคนที่มาเข้าคิวขึ้นชิงช้าสวรรค์
queue = []

# คนที่จะมาเข้าคิว
so_many_people = ['1', '2', '3', '4', '5']

# สุ่มคนมาเข้าคิวในแถวทีละคนจนครบทุกคน
enqueue_number = 1
for i in range(len(so_many_people)):
    someone = random.choice(so_many_people)
    print('Join a queue {}: {}'.format(enqueue_number, someone))
    so_many_people.remove(someone)
    queue.append(someone)
    enqueue_number += 1

# เรียกคนมาขึ้นชิงช้าสวรรค์ตามคิว
queue_number = 1
for i in range(len(queue)):
    print('Queue {}: {}'.format(queue_number, queue.pop(0)))
    queue_number += 1
