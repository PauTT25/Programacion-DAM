<?php
// guardamongo.php
// Requires: sudo apt install php-mongodb
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');

$json = null;

$document = json_decode($json, true);


$document['_created_at'] = new MongoDB\BSON\UTCDateTime(
    (int)(microtime(true) * 1000)
);


try {
    $manager = new MongoDB\Driver\Manager('mongodb://127.0.0.1:27017');

    $bulk = new MongoDB\Driver\BulkWrite();
    $id = $bulk->insert($document);

    $manager->executeBulkWrite('microtienda.pedidos', $bulk);

    echo json_encode([
        'ok' => true,
        'id' => (string)$id
    ], JSON_UNESCAPED_UNICODE);

} catch (Throwable $e) {
    http_response_code(500);
    echo json_encode([
        'ok' => false,
        'error' => $e->getMessage()
    ]);
}

