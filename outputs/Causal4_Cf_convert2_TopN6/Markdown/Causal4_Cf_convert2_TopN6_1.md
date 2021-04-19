
# Parameters

    Name :                      Causal4_Cf_convert2_TopN6-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      69758813312 function calls (69449480141 primitive calls) in 86119.00 seconds

##    Ordered by: cumulative time
   List reduced from 514 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86118.999 86118.999 {built-in method builtins.exec}
                      1    4.820    4.820 86118.999 86118.999 <string>:1(<module>)
                      1  394.149  394.149 86114.178 86114.178 main.py:79(CFagent)
                9895137   42.272    0.000 24536.738    0.002 agent.py:29(learn)
                3298379   15.386    0.000 21109.524    0.006 game.py:41(step)
                3298379   20.952    0.000 20312.090    0.006 layers.py:718(step)
                9895131  624.930    0.000 19827.933    0.002 learner.py:42(Qlearn)
                3298379  311.151    0.000 13595.133    0.004 layers.py:17(step)
              329837900  955.315    0.000 13251.471    0.000 layer.py:98(move)
        346103694/36772214 1460.966    0.000 11489.997    0.000 module.py:866(_call_impl)
               26877083   73.554    0.000 10722.227    0.000 network.py:27(forward)
                3298379  940.049    0.000 10533.355    0.003 agent.py:210(counterfact)
               26877083  354.636    0.000 10469.942    0.000 container.py:117(forward)
                3298379  382.529    0.000 9572.600    0.003 agent.py:54(_learn)
                3298379  374.251    0.000 8708.673    0.003 agent.py:202(_learn)
              329837900 1561.287    0.000 8111.615    0.000 layers.py:735(check)
                9895131   89.569    0.000 7647.221    0.001 optimizer.py:84(wrapper)
                9895131   45.237    0.000 7259.899    0.001 grad_mode.py:24(decorate_context)
                9895131  319.250    0.000 7113.834    0.001 adam.py:55(step)
                3298379 6003.159    0.002 7061.570    0.002 replaybuffer.py:22(sample_data)
                3298380  492.426    0.000 6664.078    0.002 layers.py:684(update)
                3298379 5639.775    0.002 6649.919    0.002 replaybuffer.py:67(sample_data)
                9895131 1471.486    0.000 6454.308    0.001 _functional.py:53(adam)
                3298379  105.328    0.000 6188.847    0.002 agent.py:117(_learn)
                8489395  239.161    0.000 5622.284    0.001 agent.py:49(__call__)
               52558175 5518.600    0.000 5518.600    0.000 {built-in method tensor}
               44962457   30.002    0.000 5326.051    0.000 game.py:37(board)
                9895131   40.520    0.000 5174.617    0.001 tensor.py:195(backward)
                9895131   42.650    0.000 5132.782    0.001 __init__.py:68(backward)
                3298379 2888.914    0.001 4928.870    0.001 replaybuffer.py:28(teleporter_save_data)
                9895131 4890.507    0.000 4890.507    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3298379 2499.792    0.001 4653.127    0.001 agent.py:88(interveen)
               65967590 2721.901    0.000 4633.694    0.000 layer.py:151(update)
               53754166  120.497    0.000 3868.650    0.000 conv.py:398(forward)
               53754166   77.804    0.000 3687.935    0.000 conv.py:390(_conv_forward)
               53754166 3610.131    0.000 3610.131    0.000 {built-in method conv2d}
              329837900  633.936    0.000 3517.589    0.000 layers.py:729(isFree)
               74034491  148.502    0.000 2945.175    0.000 linear.py:93(forward)
             3156048890 2392.887    0.000 2883.653    0.000 layer.py:95(isFree)
               74034491   59.209    0.000 2716.559    0.000 functional.py:1737(linear)
               74034491 2642.327    0.000 2642.327    0.000 {built-in method torch._C._nn.linear}
                1895805   42.106    0.000 2606.508    0.001 agent.py:175(choose_action)
                3298379 1648.653    0.000 2508.591    0.001 agent.py:67(modify)
              196516928 1932.699    0.000 1932.699    0.000 {built-in method clone}
               44771534 1705.565    0.000 1705.565    0.000 {built-in method cat}
             6291692038 1156.566    0.000 1652.144    0.000 enum.py:646(__hash__)
               11787774   81.102    0.000 1595.543    0.000 agent.py:59(modify_board)
              100911574  101.750    0.000 1551.804    0.000 activation.py:713(forward)
                3298373   63.158    0.000 1514.281    0.000 agent.py:171(__call__)
              329650274  336.020    0.000 1506.555    0.000 {built-in method builtins.any}
              100911574   84.091    0.000 1450.054    0.000 functional.py:1364(leaky_relu)
                3298379   58.900    0.000 1420.580    0.000 agent.py:112(__call__)
              100911574 1350.702    0.000 1350.702    0.000 {built-in method torch._C._nn.leaky_relu}
                3486106   43.771    0.000 1305.792    0.000 layers.py:740(restart)
              329837900  975.046    0.000 1296.579    0.000 layers.py:77(check)
              184709104 1261.427    0.000 1261.427    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3298379  979.806    0.000 1236.745    0.000 replaybuffer.py:73(CF_save_data)
              329837900  759.805    0.000 1185.188    0.000 layers.py:246(check)
             3589870834  965.429    0.000 1170.535    0.000 layers.py:700(<genexpr>)
                9895131  204.822    0.000 1129.407    0.000 optimizer.py:189(zero_grad)
             1171752048 1123.727    0.000 1123.727    0.000 layer.py:146(elements)
              184709104 1121.342    0.000 1121.342    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              329837900  640.686    0.000 1059.463    0.000 layers.py:286(check)
               11787774 1057.991    0.000 1057.991    0.000 {built-in method torch._C._nn.one_hot}
                3486106   21.505    0.000  918.488    0.000 level.py:8(__init__)
                3298379   69.757    0.000  803.236    0.000 replaybuffer.py:18(stacker)
              329838000  111.259    0.000  776.419    0.000 {built-in method builtins.all}
                3298373   65.809    0.000  764.128    0.000 replaybuffer.py:63(stacker)
             8275448949  756.098    0.000  756.098    0.000 layer.py:91(positions)
              329837900  563.879    0.000  739.668    0.000 layers.py:62(check)
               92354552  734.461    0.000  734.461    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3486106  120.989    0.000  732.858    0.000 levels.py:199(generate)
             1220314440  320.155    0.000  704.517    0.000 layers.py:690(<genexpr>)
               92354552  640.478    0.000  640.478    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        8605619555/8605619552  563.495    0.000  626.154    0.000 {built-in method builtins.len}
               92354552  602.189    0.000  602.189    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               92354552  598.565    0.000  598.565    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              329837900  375.648    0.000  575.800    0.000 layers.py:273(check)
                8489395  205.723    0.000  567.429    0.000 exploration.py:53(softmaxer)
              329837900  363.930    0.000  560.185    0.000 layers.py:313(check)
               13568970  212.276    0.000  545.997    0.000 random.py:315(sample)
              646481948  433.528    0.000  533.923    0.000 tensor.py:906(grad)
                3298379  295.012    0.000  501.007    0.000 collector.py:46(collect)
                6972212   58.607    0.000  496.159    0.000 level.py:41(notUsed)
             6291729589  495.585    0.000  495.585    0.000 {built-in method builtins.hash}
                1895805  428.420    0.000  483.852    0.000 agent.py:186(convert_values)
              329837900  306.906    0.000  454.406    0.000 layers.py:48(check)
                9895131   16.692    0.000  445.452    0.000 loss.py:527(forward)
               92354552  441.874    0.000  441.874    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                9895131   43.997    0.000  428.761    0.000 functional.py:2898(mse_loss)
              211603075  421.961    0.000  421.961    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              329837900  240.268    0.000  359.064    0.000 layers.py:23(check)
               34861060   48.740    0.000  331.597    0.000 layer.py:69(restart)
              322952254  233.482    0.000  325.075    0.000 layer.py:126(remove)
              521132051  225.166    0.000  305.086    0.000 layer.py:130(add)
             3641973597  288.427    0.000  288.427    0.000 {method 'random' of '_random.Random' objects}
              415889610  187.575    0.000  276.851    0.000 random.py:250(_randbelow_with_getrandbits)
                6596760  271.128    0.000  271.128    0.000 {built-in method nonzero}
               65967590  269.132    0.000  269.132    0.000 layer.py:163(<listcomp>)
             2547819264  269.083    0.000  269.083    0.000 layer.py:203(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9533959: <Causal4_Cf_convert2_TopN6_1> in cluster <dcc> Done

Job <Causal4_Cf_convert2_TopN6_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr 18 20:20:07 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr 18 20:20:08 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 20:20:08 2021
Terminated at Mon Apr 19 20:15:42 2021
Results reported at Mon Apr 19 20:15:42 2021

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

    CPU time :                                   85908.65 sec.
    Max Memory :                                 9479 MB
    Average Memory :                             6391.54 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6905.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86240 sec.
    Turnaround time :                            86135 sec.

The output (if any) is above this job summary.

