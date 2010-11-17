
<?php slot::start('head') ?>
    <title>Crash Data for Mozilla <?php out::H($product) ?>
        <?php if (isset($version) && !empty($version)) { ?>
            <?php out::H($version); ?>
        <?php } ?>
    </title>
<?php slot::end() ?>

<?php
echo html::stylesheet(array('css/daily.css'), array('screen', 'screen'));
echo html::script(
  array(
    'js/flot-0.5/jquery.flot.pack.js',
    'js/socorro/daily.js',
    'js/socorro/dashboard.js',		
    'js/socorro/topcrashers.js'
  )
);
echo "<h1>Error - no data found for $product</h1>"
?>