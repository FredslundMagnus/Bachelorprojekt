
# Parameters

    Name :                      causal4_CF_convert1_2-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      58057206673 function calls (57745705462 primitive calls) in 86113.36 seconds

##    Ordered by: cumulative time
   List reduced from 507 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.358 86113.358 {built-in method builtins.exec}
                      1    5.413    5.413 86113.357 86113.357 <string>:1(<module>)
                      1  295.015  295.015 86107.945 86107.945 main.py:96(CFagent)
                9869595   47.481    0.000 25610.209    0.003 agent.py:29(learn)
                9869590  645.275    0.000 20647.113    0.002 learner.py:42(Qlearn)
                3289865   20.985    0.000 19681.801    0.006 game.py:35(step)
                3289865   21.178    0.000 18871.778    0.006 layers.py:448(step)
                3289865  327.465    0.000 12986.842    0.004 layers.py:17(step)
              328871996  902.198    0.000 12624.219    0.000 layer.py:84(move)
        348424025/36924505 1512.789    0.000 11988.327    0.000 module.py:866(_call_impl)
                3289865 1145.801    0.000 11643.811    0.004 agent.py:204(counterfact)
               27054915   75.290    0.000 11168.631    0.000 network.py:24(forward)
               27054915  377.228    0.000 10898.731    0.000 container.py:117(forward)
                3289865  412.142    0.000 10013.946    0.003 agent.py:54(_learn)
                3289865  403.667    0.000 9064.787    0.003 agent.py:196(_learn)
                9869590  100.023    0.000 7962.468    0.001 optimizer.py:84(wrapper)
                9869590   54.065    0.000 7549.018    0.001 grad_mode.py:24(decorate_context)
                9869590  342.449    0.000 7378.823    0.001 adam.py:55(step)
              328871996 1118.720    0.000 7191.957    0.000 layers.py:465(check)
                9869590 1553.940    0.000 6680.545    0.001 _functional.py:53(adam)
                3289865 5362.605    0.002 6642.701    0.002 replaybuffer.py:22(sample_data)
                3289865  110.665    0.000 6459.739    0.002 agent.py:115(_learn)
                3289865 3687.400    0.001 6254.951    0.002 replaybuffer.py:28(teleporter_save_data)
                8591054  281.801    0.000 5938.324    0.001 agent.py:49(__call__)
                3289866  384.438    0.000 5826.794    0.002 layers.py:419(update)
               53372083 5664.977    0.000 5664.977    0.000 {built-in method tensor}
                3289865 4416.859    0.001 5525.068    0.002 replaybuffer.py:49(sample_data)
               45796094   30.963    0.000 5471.996    0.000 game.py:31(board)
                9869590   45.047    0.000 5429.564    0.001 tensor.py:195(backward)
                9869590   53.491    0.000 5382.923    0.001 __init__.py:68(backward)
               65797310 3158.705    0.000 5353.953    0.000 layer.py:129(update)
                9869590 5117.914    0.001 5117.914    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3289865 2642.945    0.001 4859.955    0.001 agent.py:86(interveen)
               54109830  126.822    0.000 4042.620    0.000 conv.py:398(forward)
              328785459  767.722    0.000 3915.852    0.000 layers.py:459(isFree)
               54109830   97.030    0.000 3848.489    0.000 conv.py:390(_conv_forward)
               54109830 3751.459    0.000 3751.459    0.000 {built-in method conv2d}
             3103577119 2645.681    0.000 3148.130    0.000 layer.py:81(isFree)
               74585015  159.352    0.000 3050.695    0.000 linear.py:93(forward)
               74585015   63.912    0.000 2801.993    0.000 functional.py:1737(linear)
                2014546   43.938    0.000 2739.022    0.001 agent.py:168(choose_action)
               74585015 2722.104    0.000 2722.104    0.000 {built-in method torch._C._nn.linear}
              241939222 2420.123    0.000 2420.123    0.000 {built-in method clone}
                3289865 1395.086    0.000 2325.237    0.001 agent.py:67(modify)
               48069409 1956.592    0.000 1956.592    0.000 {built-in method cat}
               11880919   87.249    0.000 1634.626    0.000 agent.py:59(modify_board)
              101639930   97.681    0.000 1618.186    0.000 activation.py:713(forward)
                3289860   73.564    0.000 1573.740    0.000 agent.py:164(__call__)
              101639930   87.265    0.000 1520.505    0.000 functional.py:1364(leaky_relu)
                4303168   55.011    0.000 1499.231    0.000 layers.py:469(restart)
             5677285034 1039.593    0.000 1493.823    0.000 enum.py:646(__hash__)
                3289865   70.016    0.000 1461.750    0.000 agent.py:110(__call__)
              101639930 1415.642    0.000 1415.642    0.000 {built-in method torch._C._nn.leaky_relu}
             1299222696 1363.780    0.000 1363.780    0.000 layer.py:124(elements)
              328871996  847.705    0.000 1315.009    0.000 layers.py:233(check)
              184232340 1308.622    0.000 1308.622    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                9869590  214.337    0.000 1158.272    0.000 optimizer.py:189(zero_grad)
              328871996  701.394    0.000 1141.847    0.000 layers.py:270(check)
              184232340 1139.909    0.000 1139.909    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11880919 1081.074    0.000 1081.074    0.000 {built-in method torch._C._nn.one_hot}
              328871996  814.933    0.000 1043.779    0.000 layers.py:67(check)
                4303168   26.033    0.000 1011.901    0.000 level.py:8(__init__)
              328986600  139.063    0.000 1007.005    0.000 {built-in method builtins.all}
                3289865   86.368    0.000 1006.471    0.000 replaybuffer.py:18(stacker)
             1503911854  397.363    0.000  907.600    0.000 layers.py:425(<genexpr>)
                3289865  409.688    0.000  905.137    0.000 replaybuffer.py:55(CF_save_data)
                3289860   85.504    0.000  847.764    0.000 replaybuffer.py:45(stacker)
                4303168  151.568    0.000  825.524    0.000 levels.py:199(generate)
              328871996  630.895    0.000  802.137    0.000 layers.py:56(check)
               92116170  755.258    0.000  755.258    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             7792328012  704.471    0.000  704.471    0.000 layer.py:77(positions)
               92116170  675.446    0.000  675.446    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              328871996  434.539    0.000  631.203    0.000 layers.py:257(check)
                8591054  223.572    0.000  620.125    0.000 exploration.py:53(softmaxer)
               92116170  612.679    0.000  612.679    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92116170  609.269    0.000  609.269    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               15186066  231.795    0.000  594.844    0.000 random.py:315(sample)
        7929491494/7929491491  519.215    0.000  586.348    0.000 {built-in method builtins.len}
              328871996  378.558    0.000  577.936    0.000 layers.py:294(check)
              644813274  439.599    0.000  542.813    0.000 tensor.py:906(grad)
                8606336   64.032    0.000  528.067    0.000 level.py:41(notUsed)
              257110001  527.341    0.000  527.341    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3289865  304.829    0.000  517.318    0.000 collector.py:54(collect)
                9869590   18.498    0.000  485.441    0.000 loss.py:527(forward)
              328871996  324.922    0.000  468.713    0.000 layers.py:42(check)
                9869590   55.636    0.000  466.943    0.000 functional.py:2898(mse_loss)
             5677322473  454.237    0.000  454.237    0.000 {built-in method builtins.hash}
               92116170  453.665    0.000  453.665    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9869596  433.154    0.000  433.154    0.000 {built-in method nonzero}
               43031680   62.089    0.000  417.976    0.000 layer.py:58(restart)
                2014546  409.299    0.000  409.299    0.000 agent.py:179(convert_values)
              339625380  288.168    0.000  400.774    0.000 layer.py:104(remove)
              585530968  261.890    0.000  354.724    0.000 layer.py:108(add)
              170292550  223.391    0.000  323.220    0.000 layers.py:100(isDone)
              443431717  213.911    0.000  316.907    0.000 random.py:250(_randbelow_with_getrandbits)
               65797310  301.081    0.000  301.081    0.000 layer.py:141(<listcomp>)
                9869590  277.121    0.000  277.121    0.000 {built-in method torch._C._nn.mse_loss}
             2496880449  272.687    0.000  272.687    0.000 layer.py:181(isBlocking)
               54109830   40.116    0.000  263.210    0.000 flatten.py:39(forward)
                9870777  255.037    0.000  255.037    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9496006: <causal4_CF_convert1_2_0> in cluster <dcc> Done

Job <causal4_CF_convert1_2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr  5 20:00:35 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr  5 20:58:18 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr  5 20:58:18 2021
Terminated at Tue Apr  6 20:53:38 2021
Results reported at Tue Apr  6 20:53:38 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85750.92 sec.
    Max Memory :                                 9503 MB
    Average Memory :                             6406.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6881.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            89583 sec.

The output (if any) is above this job summary.

