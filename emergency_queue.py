
class Patient:
    def __init__(self, name, urgency):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name must be a nonempty string.")

        if type(urgency) is not int or not 1 <= urgency <= 10:
            raise ValueError("Urgency must be an integer from 1 to 10.")

        self.name = name
        self.urgency = urgency


class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = (
                    self.data[parent_index], self.data[index]
                )
                index = parent_index
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if (
                left < size
                and self.data[left].urgency < self.data[smallest].urgency
            ):
                smallest = left

            if (
                right < size
                and self.data[right].urgency < self.data[smallest].urgency
            ):
                smallest = right

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (
                self.data[smallest], self.data[index]
            )

            index = smallest

    def insert(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be inserted.")

        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            return None

        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        most_urgent = self.data[0]
        self.data[0] = self.data.pop()

        self.heapify_down(0)

        return most_urgent

    def print_heap(self):
        print("\nCurrent Queue:")

        if not self.data:
            print("- No patients waiting.")
            return

        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


if __name__ == "__main__":
    print("========== EMERGENCY PRIORITY QUEUE ==========")

    heap = MinHeap()

    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))

    heap.print_heap()

    next_up = heap.peek()
    print(f"\nNext Patient: {next_up.name} ({next_up.urgency})")
    assert next_up.name == "Taylor"

    served = heap.remove_min()
    print(f"Patient Served: {served.name}")
    assert served.name == "Taylor"

    heap.print_heap()
    assert heap.peek().name == "Jordan"

    print("\n========== ADDITIONAL TESTS ==========")

    heap.insert(Patient("Morgan", 2))
    heap.insert(Patient("Riley", 1))
    heap.insert(Patient("Casey", 4))

    heap.print_heap()

    priorities = []
    while heap.peek() is not None:
        patient = heap.remove_min()
        priorities.append(patient.urgency)
        print(f"Serving: {patient.name} ({patient.urgency})")

    assert priorities == sorted(priorities)
    assert heap.peek() is None
    assert heap.remove_min() is None

    print("\nTesting equal urgency scores...")

    equal_heap = MinHeap()
    equal_heap.insert(Patient("Alex", 2))
    equal_heap.insert(Patient("Sam", 2))
    equal_heap.insert(Patient("Jamie", 1))

    assert equal_heap.remove_min().name == "Jamie"
    assert equal_heap.remove_min().urgency == 2
    assert equal_heap.remove_min().urgency == 2

    print("\nTesting invalid urgency scores...")

    for invalid_score in (0, 11, 2.5, "high"):
        try:
            Patient("Invalid Patient", invalid_score)
            raise AssertionError("Invalid urgency was accepted.")
        except ValueError:
            print(f"Correctly rejected urgency: {invalid_score}")

    print("\nAll MinHeap tests passed!")
