class StudentResult:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Dodaje ocenu u listu ocena. Baca grešku za ocene van opsega."""
        if grade < 6 or grade > 10:
            raise ValueError("Ocena mora biti između 6 i 10.")  # Bacanje greške
        self.grades.append(grade)
        
    def average(self):
        """Vraća prosečnu ocenu ili None ako nema ocena."""
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def all_passed(self):
        """Proverava da li su svi ispiti položeni (ocena mora biti 6 ili više)."""
        if not self.grades:
            return False
        return all(grade >= 6 for grade in self.grades)
