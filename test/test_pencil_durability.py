from pencil_durability import Paper

class TestPaper():
  def test_can_write_a_string(self):
    paper = Paper()
    paper.write('a string')
    assert paper.contents == 'a string'
