class PriorityQueue(object):

    items = 0
    def __init__(self):
        self.waiters = []
        self.size = len(self.waiters)


    def add(self, q_thing):
        # Insert based on priority
        # Prioritize LOW numbers
        count = 0
        while count < len(self):
            # Switched to prioritize LOW numbers
            if self.waiters[count].priority > q_thing.priority:
                self.waiters.insert(count, q_thing)
                return 'Adding ' + str(q_thing)
            else:
                count += 1
                #print 'else'

        else:
            self.waiters.append(q_thing)
            return 'Adding ' + str(q_thing)


    def top_priority(self):
        curr_top = None
        for i in self.waiters:
            if curr_top < i.priority:
                curr_top = i.priority

        return curr_top


    def remove(self):
        # Evaluate priority
            # pop 0 - priority is evaluated in the add() function
        return self.waiters.pop(0)


    def __len__(self):
        return len(self.waiters)


    def __str__(self):
        strang = ''
        for x in self.waiters:
            strang += str(x) + '\n'
        return strang + '\n'


    def __iter__(self):
        return iter(self.waiters)



class Q_item(object):
    def __init__(self, thing, priority):
            self.thing = thing
            self.priority = priority
            self.index = PriorityQueue.items
            PriorityQueue.items += 1

    def __str__(self):
        return '%d %s' % (self.priority, self.thing)

    def __add__(self, q2):
        new_item = Q_item(self.thing, self.priority)
        new_item.thing += q2.thing
        new_item.priority += q2.priority

        return new_item