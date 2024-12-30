type number =
  |Int of int
  |String of string

let parse (fileName: string) (is_int: bool) : (number list) list =
  let ic = open_in fileName in
  let rec read_lines ic acc =
    try
      let line = input_line ic in
      let numbers = 
        if is_int
        then
          List.filter_map (fun x ->
            if x = "" then None
            else
              try
                let num = int_of_string x in
                Some (Int num)
              with Failure _ ->
                Printf.printf "Invalid integer: %s\n" x;
                failwith ("Invalid integer: " ^x)
          ) (String.split_on_char ' ' line)
        else
          List.map (fun x -> String x) (String.split_on_char ' ' line)
        in
      read_lines ic (numbers :: acc)
    with
    |End_of_file ->
      close_in ic;
      List.rev acc
    |Failure msg ->
      close_in ic;
      failwith ("Failure: " ^ msg);
    |Sys_error msg ->
      close_in ic;
      failwith ("Sys_error: " ^ msg);
    |Invalid_argument msg ->
      close_in ic;
      failwith ("Invalid_argument: " ^ msg);
    |_ ->
      close_in ic;
      failwith "Unknown error";
  in
  read_lines ic []

let convert_to_int_list (data: (number list) list) : (int list) list =
  List.map (fun lst ->
    List.filter_map (function
      | Int n -> Some n
      | String _ -> None
    ) lst
  ) data

let convert_to_string_list (data: (number list) list) : (string list) list =
  List.map (fun lst ->
    List.filter_map (function
      | Int _ -> None
      | String s ->
        if s = ""
        then None
        else Some s
    ) lst
  ) data

let rec group_by (acc: 'a list) (l: 'a list list) : 'a list list -> 'a list list = function
  |[] -> acc::l
  |[]::q -> (
      group_by [] (acc::l) q
    )
  |t::q -> (
      group_by (acc@t) l q
    )