let rec count (e: char) : char list -> int = function
  |[] -> 0
  |x::xs ->
    if x = e
    then 1 + (count e xs)
    else count e xs

let is_valide (i_min: int) (i_max: int) (e: string) (password: string) : bool =
  let n = count (String.get e 0) (List.of_seq (String.to_seq password)) in
  i_min <= n && n <= i_max

let is_valide_2 (i1: int) (i2: int) (e: string) (password: string) : bool =
  let letter = (String.get e 0) in
  let b1 = (password.[i1-1] = letter) in
  let b2 = (password.[i2-1] = letter) in
  not (b1 = b2)

let rec main1 : string list list -> int = function
  |[] -> 0
  |[imin; imax; e; password]::q ->
    if is_valide (int_of_string imin) (int_of_string imax) e password
    then 1 + (main1 q)
    else main1 q
  |_ -> failwith "parsing error"

let rec main2 : string list list -> int = function
    |[] -> 0
    |[i1; i2; e; password]::q ->
      if is_valide_2 (int_of_string i1) (int_of_string i2) e password
      then 1 + (main2 q)
      else main2 q
    |_ -> failwith "parsing error"

let () =
  let parsed_data = 
    if Sys.argv.(1) = "test"
    then
      Parse.convert_to_string_list (Parse.parse "2020/2/test.txt" false)
    else
      Parse.convert_to_string_list (Parse.parse "2020/2/data.txt" false)
    in
  let x =
    if Sys.argv.(2) = "1"
    then main1 parsed_data
    else main2 parsed_data
  in
  Printf.printf "%d" x