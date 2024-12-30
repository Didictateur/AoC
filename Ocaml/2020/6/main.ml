let rec main1 (l: string list list) : int =
  let group = Parse.group_by l in
  0

let rec main2 (l: string list list) : int =
  0

let () =
  let parsed_data = 
    if Sys.argv.(1) = "test"
    then
      Parse.convert_to_string_list (Parse.parse "2020/6/test.txt" false)
    else
      Parse.convert_to_string_list (Parse.parse "2020/6/data.txt" false)
    in
  let x =
    if Sys.argv.(2) = "1"
    then main1 parsed_data
    else main2 parsed_data
  in
  Printf.printf "%d" x