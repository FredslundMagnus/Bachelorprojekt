
# Parameters

    Name :                      causal3_9x9-1
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.04
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      34317432658 function calls (34170913115 primitive calls) in 42914.10 seconds

##    Ordered by: cumulative time
   List reduced from 476 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42914.098 42914.098 {built-in method builtins.exec}
                      1    1.941    1.941 42914.098 42914.098 <string>:1(<module>)
                      1  121.619  121.619 42912.156 42912.156 main.py:43(teleport)
                5233292   18.160    0.000 14665.981    0.003 agent.py:27(learn)
                5233292  383.282    0.000 12565.573    0.002 learner.py:42(Qlearn)
                2616646   11.032    0.000 10645.272    0.004 game.py:27(step)
                2616646   14.352    0.000 10033.227    0.004 layers.py:475(step)
                2616646   89.562    0.000 8767.315    0.003 agent.py:51(_learn)
                2616646  197.730    0.000 6424.570    0.002 layers.py:18(step)
              261664600  301.338    0.000 6205.944    0.000 layer.py:76(move)
                2616646 3301.977    0.001 6016.162    0.002 replaybuffer.py:27(teleporter_save_data)
        164833917/18315385  656.089    0.000 5999.240    0.000 module.py:866(_call_impl)
                2616646   74.383    0.000 5868.441    0.002 agent.py:110(_learn)
               13082093   37.284    0.000 5589.463    0.000 network.py:24(forward)
               13082093  177.709    0.000 5469.249    0.000 container.py:117(forward)
                5233292   44.384    0.000 5242.410    0.001 optimizer.py:84(wrapper)
                5233292   22.108    0.000 5031.676    0.001 grad_mode.py:24(decorate_context)
                5233292  145.794    0.000 4960.859    0.001 adam.py:55(step)
                5233292 1027.303    0.000 4646.000    0.001 _functional.py:53(adam)
                2616646 2527.288    0.001 4353.498    0.002 agent.py:81(interveen)
              261664600  626.841    0.000 3797.081    0.000 layers.py:492(check)
                5232155  127.688    0.000 3718.037    0.001 agent.py:46(__call__)
                2616647  265.435    0.000 3576.087    0.001 layers.py:446(update)
                5233292   21.349    0.000 3165.736    0.001 tensor.py:195(backward)
                5233292   20.936    0.000 3143.551    0.001 __init__.py:68(backward)
                2616646 2175.921    0.001 3109.571    0.001 replaybuffer.py:23(sample_data)
                5233292 3006.367    0.001 3006.367    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              185732600 2200.856    0.000 2200.856    0.000 {built-in method clone}
               26164186   57.253    0.000 2007.067    0.000 conv.py:398(forward)
                2616646 1203.285    0.000 1984.203    0.001 agent.py:63(modify)
               26164186   34.245    0.000 1923.868    0.000 conv.py:390(_conv_forward)
               26164186 1889.623    0.000 1889.623    0.000 {built-in method conv2d}
              261664600  369.971    0.000 1846.002    0.000 layers.py:486(isFree)
               34012987   70.571    0.000 1554.425    0.000 linear.py:93(forward)
             1946185086 1194.497    0.000 1476.031    0.000 layer.py:73(isFree)
               34012987   28.835    0.000 1450.804    0.000 functional.py:1737(linear)
               23549823  809.483    0.000 1430.481    0.000 layer.py:137(NoRock_update)
               34012987 1414.799    0.000 1414.799    0.000 {built-in method torch._C._nn.linear}
                2616646   37.519    0.000 1148.470    0.000 agent.py:105(__call__)
                7848801   52.954    0.000 1117.849    0.000 agent.py:55(modify_board)
                4168814   41.271    0.000 1114.543    0.000 layers.py:496(restart)
               94199256  945.256    0.000  945.256    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               23548677  937.467    0.000  937.467    0.000 {built-in method cat}
             3893339559  639.345    0.000  907.648    0.000 enum.py:646(__hash__)
               47095080   39.380    0.000  879.047    0.000 activation.py:713(forward)
               10819393  857.695    0.000  857.695    0.000 {built-in method tensor}
               47095080   40.239    0.000  839.667    0.000 functional.py:1364(leaky_relu)
               94199256  830.826    0.000  830.826    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               47095080  791.070    0.000  791.070    0.000 {built-in method torch._C._nn.leaky_relu}
              261664600  485.272    0.000  772.279    0.000 layers.py:302(check)
                2616646   49.769    0.000  753.025    0.000 replaybuffer.py:19(stacker)
                5233292  119.528    0.000  741.878    0.000 optimizer.py:189(zero_grad)
              261664600  450.385    0.000  737.150    0.000 layers.py:261(check)
                4168814   20.422    0.000  715.004    0.000 level.py:8(__init__)
                7848801  714.073    0.000  714.073    0.000 {built-in method torch._C._nn.one_hot}
                5233292    6.070    0.000  687.965    0.000 game.py:23(board)
              261664700   74.356    0.000  667.780    0.000 {built-in method builtins.all}
              853090433  196.427    0.000  622.805    0.000 layers.py:452(<genexpr>)
                4168814  103.813    0.000  619.117    0.000 levels.py:163(generate)
              193581401  594.360    0.000  594.360    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2616646  316.347    0.000  525.646    0.000 collector.py:54(collect)
               47099628  514.746    0.000  514.746    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              261664600  351.956    0.000  471.961    0.000 layers.py:63(check)
               47099628  453.772    0.000  453.772    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               47099628  432.182    0.000  432.182    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               47099628  427.869    0.000  427.869    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              261664600  270.789    0.000  425.020    0.000 layers.py:328(check)
             5050622144  418.205    0.000  418.205    0.000 layer.py:69(positions)
                8337628   50.388    0.000  415.254    0.000 level.py:41(notUsed)
             1018774187  399.697    0.000  399.697    0.000 layer.py:116(elements)
              261664700  262.999    0.000  394.298    0.000 layers.py:110(isDone)
                5232155  143.767    0.000  393.256    0.000 exploration.py:53(softmaxer)
              261664600  242.154    0.000  382.648    0.000 layers.py:287(check)
               37519326   47.674    0.000  346.775    0.000 layer.py:50(restart)
               47099628  334.870    0.000  334.870    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              261664600  212.993    0.000  317.573    0.000 layers.py:47(check)
              329697450  224.755    0.000  279.663    0.000 tensor.py:906(grad)
             3893358750  268.306    0.000  268.306    0.000 {built-in method builtins.hash}
                5233292    7.555    0.000  253.869    0.000 loss.py:527(forward)
              486536219  181.012    0.000  246.498    0.000 layer.py:100(add)
                5233292   20.584    0.000  246.314    0.000 functional.py:2898(mse_loss)
               10954274   87.461    0.000  228.821    0.000 random.py:315(sample)
        2522628652/2522628650  185.466    0.000  223.963    0.000 {built-in method builtins.len}
               15699876  220.758    0.000  220.758    0.000 {built-in method sum}
              175086761  213.056    0.000  213.056    0.000 level.py:32(inverse)
                4168914   99.913    0.000  200.662    0.000 layers.py:33(reset)
              238178960  110.759    0.000  170.789    0.000 layer.py:96(remove)
                5233292  162.349    0.000  162.349    0.000 {built-in method torch._C._nn.mse_loss}
             1517259588  154.745    0.000  154.745    0.000 layer.py:177(isBlocking)
               26164186   17.202    0.000  149.286    0.000 flatten.py:39(forward)
                5234076  143.672    0.000  143.672    0.000 {built-in method max}
                7849938   10.922    0.000  143.427    0.000 tensor.py:525(__rsub__)
               26164186  132.084    0.000  132.084    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7849938  130.452    0.000  130.452    0.000 {built-in method rsub}
                5232155  124.840    0.000  124.840    0.000 {built-in method multinomial}
                8337628    7.281    0.000  117.460    0.000 level.py:38(elementsIn)
              184533931   80.064    0.000  116.398    0.000 random.py:250(_randbelow_with_getrandbits)
             1582314370  115.573    0.000  115.573    0.000 {method 'append' of 'list' objects}
              167451609  113.793    0.000  113.793    0.000 {built-in method torch._C._get_tracing_state}
                5233292   21.338    0.000  111.934    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9458195: <causal3_9x9_1> in cluster <dcc> Done

Job <causal3_9x9_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 01:18:04 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 01:18:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 01:18:05 2021
Terminated at Thu Mar 25 13:13:30 2021
Results reported at Thu Mar 25 13:13:30 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   42799.39 sec.
    Max Memory :                                 6258 MB
    Average Memory :                             4587.15 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1934.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42947 sec.
    Turnaround time :                            42926 sec.

The output (if any) is above this job summary.

