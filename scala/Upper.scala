object Upper {
  def main(args: Array[String]) = {
    args.map(_.toUpperCase()).foreach(printf("%s ", _))
    println("")
  }
}

// vim: set ts=4 sw=4 et:
