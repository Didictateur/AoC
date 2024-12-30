let rec compare (total: int) (x: int) : int list list -> int*int = function
  |[] -> (0, 0)
  |[]::q -> compare total x q
  |[a]::q ->
    if x+a = total
    then (x, a)
    else compare total x q
  |_ -> failwith "Not well parsed"

let rec search (total: int) (l: int list list) : (int list list) -> int = function
  |[] -> failwith "No solution found"
  |[]::q -> search total l q
  |[a]::q ->
    (match (compare total a l) with
      |(0, 0) -> search total l q
      |(x, y) -> x*y)
  |_ -> failwith "Very bad parse"

let rec sum_to (total: int) (l: int list list) : (int list list) -> int = function
    |[] -> failwith "Not found"
    |[]::q -> sum_to total l q
    |[a]::q when a >= total -> sum_to total l q
    |[a]::q -> (
      try
        match (search (total - a) l l) with
          |0 -> sum_to total l q
          |x -> x*a
      with
        |_ -> sum_to total l q)
    |_ -> failwith "Very very bad parsing"

let main1 (parsed_data: int list list) : int =
  search 2020 parsed_data parsed_data

let main2 (parsed_data: int list list) : int =
  sum_to 2020 parsed_data parsed_data

let () =
  let parsed_data = 
    if Sys.argv.(1) = "test"
    then
      Parse.convert_to_int_list (Parse.parse "2020/1/test.txt" true)
    else
      Parse.convert_to_int_list (Parse.parse "2020/1/data.txt" true)
    in
  let x =
    if Sys.argv.(2) = "1"
    then main1 parsed_data
    else main2 parsed_data
  in
  Printf.printf "%d" x